#include <pebble.h>
#include "course_display.h"
/* Pocket Field Guide C1: previous API checkpoints remain in this starter. */
static Window *s_window;static TextLayer *s_title;
static MenuLayer *s_menu;
static const char *s_species[]={"Heron","Chickadee","Sunfish","Fox","Map","Notes"};
static uint16_t rows(MenuLayer *m,uint16_t section,void *c){(void)m;(void)section;(void)c;return 6;}
static void draw_row(GContext *ctx,const Layer *cell,MenuIndex *i,void *c){
 (void)c;menu_cell_basic_draw(ctx,cell,s_species[i->row],NULL,NULL);
}
static void select_row(MenuLayer *m,MenuIndex *i,void *c){
 (void)m;(void)c;text_layer_set_text(s_title,s_species[i->row]);
}




static void load(Window *w){
 Layer *root=window_get_root_layer(w);GRect b=layer_get_bounds(root);
 GRect safe=course_content_rect(b);
 s_title=text_layer_create(GRect(safe.origin.x, safe.origin.y,
     safe.size.w, 30));
 text_layer_set_text_alignment(s_title,GTextAlignmentCenter);
 text_layer_set_text(s_title,"FIELD GUIDE");
 layer_add_child(root,text_layer_get_layer(s_title));
 s_menu=menu_layer_create(GRect(safe.origin.x,
     safe.origin.y+32, safe.size.w, safe.size.h-32));
 menu_layer_set_callbacks(s_menu,NULL,(MenuLayerCallbacks){
  .get_num_rows=rows,.draw_row=draw_row,.select_click=select_row
 });
 menu_layer_set_click_config_onto_window(s_menu,w);
 layer_add_child(root,menu_layer_get_layer(s_menu));
 
 
 
 
}
static void unload(Window *w){
 (void)w;
 
 
 
 menu_layer_destroy(s_menu);
 text_layer_destroy(s_title);
}
static void init(void){
 s_window=window_create();
 window_set_window_handlers(s_window,(WindowHandlers){.load=load,.unload=unload});
 window_stack_push(s_window,true);
}
static void deinit(void){window_destroy(s_window);}
int main(void){init();app_event_loop();deinit();}
