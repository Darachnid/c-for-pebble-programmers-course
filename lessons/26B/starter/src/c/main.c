#include <pebble.h>
/* Pocket Field Guide C0: previous API checkpoints remain in this starter. */
static Window *s_window;static TextLayer *s_title;





static void load(Window *w){
 Layer *root=window_get_root_layer(w);GRect b=layer_get_bounds(root);
 s_title=text_layer_create(GRect(4,4,b.size.w-8,34));
 text_layer_set_text_alignment(s_title,GTextAlignmentCenter);
 text_layer_set_text(s_title,"FIELD GUIDE");
 layer_add_child(root,text_layer_get_layer(s_title));
 
 
 
 
 
}
static void unload(Window *w){
 (void)w;
 
 
 
 
 text_layer_destroy(s_title);
}
static void init(void){
 s_window=window_create();
 window_set_window_handlers(s_window,(WindowHandlers){.load=load,.unload=unload});
 window_stack_push(s_window,true);
}
static void deinit(void){window_destroy(s_window);}
int main(void){init();app_event_loop();deinit();}
