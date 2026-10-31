#include <pebble.h>
/* Pocket Field Guide C2: previous API checkpoints remain in this starter. */
static Window *s_window;static TextLayer *s_title;
static int s_selected=0;
static Layer *s_canvas;
static MenuLayer *s_menu;
static const char *s_species[]={"Heron","Chickadee","Sunfish","Fox","Map","Notes"};
static uint16_t rows(MenuLayer *m,uint16_t section,void *c){(void)m;(void)section;(void)c;return 6;}
static void draw_row(GContext *ctx,const Layer *cell,MenuIndex *i,void *c){
 (void)c;menu_cell_basic_draw(ctx,cell,s_species[i->row],NULL,NULL);
}
static void select_row(MenuLayer *m,MenuIndex *i,void *c){
 (void)m;(void)c;
 s_selected=i->row;
 text_layer_set_text(s_title,s_species[i->row]);
 
 if(s_canvas)layer_mark_dirty(s_canvas);
 
}

static void draw_canvas(Layer *layer,GContext *ctx){
 GRect b=layer_get_bounds(layer);
 graphics_context_set_stroke_color(ctx,GColorBlack);
 graphics_draw_circle(ctx,GPoint(b.size.w/2,30),18+(s_selected%3)*4);
 graphics_draw_line(ctx,GPoint(10,76),GPoint(b.size.w-10,76));
 
}


static void load(Window *w){
 Layer *root=window_get_root_layer(w);GRect b=layer_get_bounds(root);
 s_title=text_layer_create(GRect(4,4,b.size.w-8,34));
 text_layer_set_text_alignment(s_title,GTextAlignmentCenter);
 text_layer_set_text(s_title,"FIELD GUIDE");
 layer_add_child(root,text_layer_get_layer(s_title));
 s_menu=menu_layer_create(GRect(0,42,b.size.w,90));
 menu_layer_set_callbacks(s_menu,NULL,(MenuLayerCallbacks){
  .get_num_rows=rows,.draw_row=draw_row,.select_click=select_row
 });
 menu_layer_set_click_config_onto_window(s_menu,w);
 layer_add_child(root,menu_layer_get_layer(s_menu));
 
 s_canvas=layer_create(GRect(0,136,b.size.w,88));
 layer_set_update_proc(s_canvas,draw_canvas);
 layer_add_child(root,s_canvas);
 
 
}
static void unload(Window *w){
 (void)w;
 
 
 layer_destroy(s_canvas);
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
