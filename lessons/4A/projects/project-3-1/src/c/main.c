#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
static int s_x=100, s_y=25;
static int x_velocity=0, y_velocity=3;
const int ball_radius=12; /* Exercise: why can't this be incremented? */
static AppTimer *s_timer;
static void advance(void) {
   /* TODO: add horizontal motion using x_velocity. */
   s_y += y_velocity;
   if(s_y >= 210 - ball_radius || s_y <= ball_radius) y_velocity = -y_velocity;
 }
 static void timer_callback(void *context) {
   (void)context; advance(); layer_mark_dirty(s_canvas);
   s_timer = app_timer_register(80, timer_callback, NULL);
 }
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  graphics_fill_circle(ctx, GPoint(s_x,s_y), ball_radius);
}


static void up_click_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  /* TODO: increase ball radius and speed (after fixing const declaration). */
  layer_mark_dirty(s_canvas);
}
static void down_click_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  /* TODO: decrease ball radius and speed. */
  layer_mark_dirty(s_canvas);
}
static void click_config(void *context) {
  (void)context;
  window_single_click_subscribe(BUTTON_ID_UP, up_click_handler);
  window_single_click_subscribe(BUTTON_ID_DOWN, down_click_handler);
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
  s_timer = app_timer_register(80, timer_callback, NULL);
  s_window = window_create();
  window_set_window_handlers(s_window, (WindowHandlers){
    .load = window_load, .unload = window_unload
  });
  
  window_set_click_config_provider(s_window, click_config);
  window_stack_push(s_window, true);
  
}
static void deinit(void) {
  
  if (s_timer) app_timer_cancel(s_timer);
  window_destroy(s_window);
}
int main(void) { init(); app_event_loop(); deinit(); }
