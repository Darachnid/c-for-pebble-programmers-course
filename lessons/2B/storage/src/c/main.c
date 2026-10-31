#include <pebble.h>

/* Independent persistence pattern for integration activity 7C.
   Up increments, Down resets; value survives watchapp restart. */
#define STORAGE_KEY 202
static Window *s_window;
static TextLayer *s_title;
static TextLayer *s_count_layer;
static int s_count = 0;
static char s_buffer[16];

static void refresh(void) {
  snprintf(s_buffer, sizeof(s_buffer), "%d", s_count);
  text_layer_set_text(s_count_layer, s_buffer);
  APP_LOG(APP_LOG_LEVEL_INFO, "counter=%d", s_count);
}

static void save(void) {
  persist_write_int(STORAGE_KEY, s_count);
}

static void up_click(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer;
  (void)context;
  ++s_count;
  save();
  refresh();
}

static void down_click(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer;
  (void)context;
  s_count = 0;
  save();
  refresh();
}

static void click_config_provider(void *context) {
  (void)context;
  window_single_click_subscribe(BUTTON_ID_UP, up_click);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_click);
}

static void main_window_load(Window *window) {
  Layer *root = window_get_root_layer(window);
  GRect bounds = layer_get_bounds(root);
  s_title = text_layer_create(GRect(0, 44, bounds.size.w, 36));
  s_count_layer = text_layer_create(GRect(0, 87, bounds.size.w, 70));
  text_layer_set_text(s_title, "Up +1 / Down reset");
  text_layer_set_text_alignment(s_title, GTextAlignmentCenter);
  text_layer_set_text_alignment(s_count_layer, GTextAlignmentCenter);
  text_layer_set_font(s_title, fonts_get_system_font(FONT_KEY_GOTHIC_18_BOLD));
  text_layer_set_font(s_count_layer, fonts_get_system_font(FONT_KEY_BITHAM_42_BOLD));
  layer_add_child(root, text_layer_get_layer(s_title));
  layer_add_child(root, text_layer_get_layer(s_count_layer));
  refresh();
}

static void main_window_unload(Window *window) {
  (void)window;
  text_layer_destroy(s_count_layer);
  text_layer_destroy(s_title);
}

static void init(void) {
  if (persist_exists(STORAGE_KEY)) s_count = persist_read_int(STORAGE_KEY);
  s_window = window_create();
  window_set_background_color(s_window, GColorWhite);
  window_set_click_config_provider(s_window, click_config_provider);
  window_set_window_handlers(s_window, (WindowHandlers) {
    .load = main_window_load, .unload = main_window_unload
  });
  window_stack_push(s_window, true);
}

static void deinit(void) {
  window_destroy(s_window);
}

int main(void) {
  init();
  app_event_loop();
  deinit();
}
