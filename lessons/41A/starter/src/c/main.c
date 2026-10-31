#include <pebble.h>
/* 41A: intentionally minimal independent-app shell.
 * There is no application solution here: develop your own spec from 22C / 25C. */
static Window *s_window;
static TextLayer *s_label;
static void load(Window *window) {
 Layer *root=window_get_root_layer(window);
 GRect bounds=layer_get_bounds(root);
 s_label=text_layer_create(GRect(6,70,bounds.size.w-12,80));
 text_layer_set_text(s_label,"Independent App\nImplement your own concept");
 text_layer_set_text_alignment(s_label,GTextAlignmentCenter);
 layer_add_child(root,text_layer_get_layer(s_label));
}
static void unload(Window *window) {(void)window;text_layer_destroy(s_label);}
static void init(void) {
 s_window=window_create();
 window_set_window_handlers(s_window,(WindowHandlers){.load=load,.unload=unload});
 window_stack_push(s_window,true);
}
static void deinit(void) {window_destroy(s_window);}
int main(void) {init();app_event_loop();deinit();}
