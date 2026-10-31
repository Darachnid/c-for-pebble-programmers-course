#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
static int s_number=42; static char s_decimal[16]; static char s_binary[9]="00000000";

static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  snprintf(s_decimal,sizeof(s_decimal),"Decimal %d",s_number);
  graphics_draw_text(ctx, s_decimal, fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD), GRect(0,48,bounds.size.w,44), GTextOverflowModeTrailingEllipsis, GTextAlignmentCenter, NULL);
  graphics_draw_text(ctx, s_binary, fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD), GRect(0,112,bounds.size.w,44), GTextOverflowModeTrailingEllipsis, GTextAlignmentCenter, NULL);
}
static void up_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  s_number=(s_number+1)%256;
  /* TODO: update s_binary using a loop, then terminate with '\\0'. */
  layer_mark_dirty(s_canvas);
}
static void down_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  s_number=(s_number+255)%256;
  /* TODO: use the same conversion algorithm. */
  layer_mark_dirty(s_canvas);
}
static void click_config(void *context) {
  (void)context;
  window_single_click_subscribe(BUTTON_ID_UP, up_handler);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_handler);
}


static void window_load(Window *window) {
  Layer *root = window_get_root_layer(window);
  s_canvas = layer_create(layer_get_bounds(root));
  layer_set_update_proc(s_canvas, canvas_update);
  layer_add_child(root, s_canvas);
}
static void window_unload(Window *window) {
  (void)window;
  layer_destroy(s_canvas);
}
static void init(void) {
  
  s_window = window_create();
  window_set_window_handlers(s_window, (WindowHandlers){
    .load = window_load, .unload = window_unload
  });
  window_set_click_config_provider(s_window, click_config);
  window_stack_push(s_window, true);
  
}
static void deinit(void) {
  
  
  window_destroy(s_window);
}
int main(void) { init(); app_event_loop(); deinit(); }
