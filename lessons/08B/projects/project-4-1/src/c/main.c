#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
static int s_second=0; static char s_seconds[12];
static void mark_the_second(int second, char *label, size_t count) {
  if (second % 5 != 0) { snprintf(label,count,""); return; }
  switch(second/5) {
    case 0: snprintf(label,count,"12"); break;
    case 1: snprintf(label,count,"1"); break;
    case 2: snprintf(label,count,"2"); break;
    default: snprintf(label,count,"%d",second/5); break;
  }
 }
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  mark_the_second(s_second,s_seconds,sizeof(s_seconds));
  int32_t angle=(int32_t)s_second*TRIG_MAX_ANGLE/60;
  GPoint center=GPoint(bounds.size.w/2,bounds.size.h/2);
  GPoint hand=GPoint(center.x+(int32_t)sin_lookup(angle)*75/TRIG_MAX_RATIO,
                    center.y-(int32_t)cos_lookup(angle)*75/TRIG_MAX_RATIO);
  graphics_draw_circle(ctx,center,75);
  graphics_draw_line(ctx,center,hand);
  graphics_draw_text(ctx, s_seconds, fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD), GRect(70,18,bounds.size.w-140,36), GTextOverflowModeTrailingEllipsis, GTextAlignmentCenter, NULL);
}

static void tick_handler(struct tm *tick_time, TimeUnits units_changed) {
  (void)units_changed;
  s_second=tick_time->tm_sec;
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
  time_t now=time(NULL); s_second=localtime(&now)->tm_sec;
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
