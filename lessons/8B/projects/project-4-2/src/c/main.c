#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
static char s_time[16]; static int s_minute=0; static int s_second=0;

static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  graphics_draw_text(ctx, s_time, fonts_get_system_font(FONT_KEY_BITHAM_42_BOLD), GRect(0,bounds.size.h/2-26,bounds.size.w,60), GTextOverflowModeTrailingEllipsis, GTextAlignmentCenter, NULL);
}

static void tick_handler(struct tm *tick_time, TimeUnits units_changed) {
  (void)units_changed;
  s_minute=tick_time->tm_min; s_second=tick_time->tm_sec;
  strftime(s_time,sizeof(s_time),"%H:%M:%S",tick_time);
  /* TODO: choose visual state using if / else.
     TODO: if enabled, signal quarter-hour only when seconds == 0. */
  layer_mark_dirty(s_canvas);
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
  time_t now=time(NULL); struct tm *tm_now=localtime(&now);
  strftime(s_time,sizeof(s_time),"%H:%M:%S",tm_now);
  s_window = window_create();
  window_set_window_handlers(s_window, (WindowHandlers){
    .load = window_load, .unload = window_unload
  });
  
  window_stack_push(s_window, true);
  tick_timer_service_subscribe(SECOND_UNIT, tick_handler);
}
static void deinit(void) {
  tick_timer_service_unsubscribe();
  
  window_destroy(s_window);
}
int main(void) { init(); app_event_loop(); deinit(); }
