#include <pebble.h>
/* Original Emery-only teaching starter. Complete the TODOs yourself. */
static Window *s_window;
static Layer *s_canvas;
#define COLS 10
#define ROWS 12
static uint8_t s_cells[ROWS][COLS];
static void replace_colors(uint8_t old_color, uint8_t new_color) {
  /* TODO: nested for loops over y and x.
     If s_cells[y][x] == old_color, assign new_color. */
  (void)old_color; (void)new_color;
}
static void canvas_update(Layer *layer, GContext *ctx) {
  GRect bounds = layer_get_bounds(layer);
  graphics_context_set_fill_color(ctx, GColorWhite);
  graphics_fill_rect(ctx, bounds, 0, GCornerNone);
  graphics_context_set_fill_color(ctx, GColorBlack);
  graphics_context_set_stroke_color(ctx, GColorBlack);
  for(int y=0;y<ROWS;y++) for(int x=0;x<COLS;x++) {
    GColor cell = s_cells[y][x] ? GColorBlue : GColorYellow;
    graphics_context_set_fill_color(ctx,cell);
    graphics_fill_rect(ctx,GRect(x*18+10,y*16+12,16,14),0,GCornerNone);
  }
}
static void up_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  replace_colors(0,1);
  layer_mark_dirty(s_canvas);
}
static void down_handler(ClickRecognizerRef recognizer, void *context) {
  (void)recognizer; (void)context;
  replace_colors(1,0);
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
  for(int y=0;y<ROWS;y++) for(int x=0;x<COLS;x++) s_cells[y][x]=(x+y)%2;
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
