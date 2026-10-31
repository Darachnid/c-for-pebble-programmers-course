#include <pebble.h>
#include "course_display.h"

/* Emery font explorer; Up/Down selects among four SDK system fonts.
   Project normal. Diagnostics log the selected index. */
static Window *s_window;
static TextLayer *s_sample;
static TextLayer *s_title;
static int s_index = 0;
#define FONT_COUNT 4

static const char *FONT_KEYS[FONT_COUNT] = {
  FONT_KEY_BITHAM_42_BOLD,
  FONT_KEY_GOTHIC_28_BOLD,
  FONT_KEY_GOTHIC_24_BOLD,
  FONT_KEY_GOTHIC_18_BOLD
};
static const char *FONT_NAMES[FONT_COUNT] = {
  "Bitham 42", "Gothic 28", "Gothic 24", "Gothic 18"
};

static void apply_font(void) {
  APP_LOG(APP_LOG_LEVEL_DEBUG, "apply index=%d / count=%d", s_index, FONT_COUNT);
  text_layer_set_font(s_sample, fonts_get_system_font(FONT_KEYS[s_index]));
  text_layer_set_text(s_title, FONT_NAMES[s_index]);
}

static void up_click(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer;
  (void)context;
  int old = s_index;
  s_index = (s_index + 1) % FONT_COUNT;
  APP_LOG(APP_LOG_LEVEL_DEBUG, "UP index=%d -> %d", old, s_index);
  apply_font();
  
}

static void down_click(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer;
  (void)context;
  int old = s_index;
  s_index = (s_index + FONT_COUNT - 1) % FONT_COUNT;
  APP_LOG(APP_LOG_LEVEL_DEBUG, "DOWN index=%d -> %d", old, s_index);
  apply_font();
  
}

static void click_config_provider(void *context) {
  (void)context;
  window_single_click_subscribe(BUTTON_ID_UP, up_click);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_click);
}

static void main_window_load(Window *window) {
  Layer *root = window_get_root_layer(window);
  GRect bounds = layer_get_bounds(root);
  GRect safe = course_content_rect(bounds);
  s_sample = text_layer_create(GRect(safe.origin.x, safe.origin.y+safe.size.h/6, safe.size.w,78));
  s_title = text_layer_create(GRect(safe.origin.x, safe.origin.y+safe.size.h*3/4, safe.size.w,42));
  text_layer_set_background_color(s_sample, GColorClear);
  text_layer_set_background_color(s_title, GColorClear);
  text_layer_set_text_color(s_sample, GColorBlack);
  text_layer_set_text_color(s_title, GColorBlack);
  text_layer_set_text_alignment(s_sample, GTextAlignmentCenter);
  text_layer_set_text_alignment(s_title, GTextAlignmentCenter);
  text_layer_set_font(s_title, fonts_get_system_font(FONT_KEY_GOTHIC_18_BOLD));
  text_layer_set_text(s_sample, "Pebble");
  layer_add_child(root, text_layer_get_layer(s_sample));
  layer_add_child(root, text_layer_get_layer(s_title));
  apply_font();
}

static void main_window_unload(Window *window) {
  (void)window;
  text_layer_destroy(s_title);
  text_layer_destroy(s_sample);
}

static void init(void) {
  
  s_window = window_create();
  window_set_background_color(s_window, GColorWhite);
  window_set_click_config_provider(s_window, click_config_provider);
  window_set_window_handlers(s_window, (WindowHandlers) {
    .load = main_window_load,
    .unload = main_window_unload
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
