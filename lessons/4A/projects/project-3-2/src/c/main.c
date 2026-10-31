#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
static int s_degrees=0, s_radius=66; static AppTimer *s_timer;
static void timer_callback(void *context) {
  (void)context;
  s_degrees = (s_degrees + 2) % 360;
  layer_mark_dirty(s_canvas);
  s_timer=app_timer_register(60, timer_callback, NULL);
}
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  int32_t angle = (int32_t)s_degrees * TRIG_MAX_ANGLE / 360;
  int x=bounds.size.w/2 + (int32_t)cos_lookup(angle)*s_radius/TRIG_MAX_RATIO;
  int y=bounds.size.h/2 + (int32_t)sin_lookup(angle)*s_radius/TRIG_MAX_RATIO;
  graphics_draw_text(ctx, "A", fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD), GRect(x-20,y-18,40,36), GTextOverflowModeTrailingEllipsis, GTextAlignmentCenter, NULL);
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
  s_timer=app_timer_register(60, timer_callback, NULL);
  s_window = window_create();
  window_set_window_handlers(s_window, (WindowHandlers){
    .load = window_load, .unload = window_unload
  });
  
  window_stack_push(s_window, true);
  
}
static void deinit(void) {
  
  if(s_timer) app_timer_cancel(s_timer);
  window_destroy(s_window);
}
int main(void) { init(); app_event_loop(); deinit(); }
