#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;

static void fill_the_rectangle(GContext *ctx,GRect box) {
  /* TODO: draw a label using graphics_draw_text() inside 'box'. */
  (void)ctx; (void)box;
}
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  GRect box=GRect(18,64,bounds.size.w-36,95);
  graphics_draw_rect(ctx,box);
  fill_the_rectangle(ctx,box);
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
