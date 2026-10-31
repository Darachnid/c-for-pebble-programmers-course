#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;

static void draw_circles(GContext *ctx,GPoint center,int radius) {
  for(int r=radius;r>0;r-=12) graphics_draw_circle(ctx,center,r);
  /* TODO: replace the loop with recursion and a base case. */
}
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  GPoint center=GPoint(bounds.size.w/2,bounds.size.h/2);
 draw_circles(ctx,center,84);
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
  
  window_stack_push(s_window, true);
  
}
static void deinit(void) {
  
  
  window_destroy(s_window);
}
int main(void) { init(); app_event_loop(); deinit(); }
