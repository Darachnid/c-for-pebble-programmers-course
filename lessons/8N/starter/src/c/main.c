#include <pebble.h>
/* Pocket Field Guide C5: previous API checkpoints remain in this starter. */
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
static GPoint s_points[]={{0,-16},{12,13},{0,6},{-12,13}};
static const GPathInfo s_path_info={.num_points=4,.points=s_points};
static GPath *s_path;
static Layer *s_canvas;
static void draw_canvas(Layer *layer,GContext *ctx){
 GRect b=layer_get_bounds(layer);
 graphics_context_set_stroke_color(ctx,GColorBlack);
 graphics_draw_circle(ctx,GPoint(b.size.w/2,30),22);
 graphics_draw_line(ctx,GPoint(10,76),GPoint(b.size.w-10,76));
 gpath_draw_outline(ctx,s_path);
}
static GBitmap *s_bitmap;static BitmapLayer *s_bitmap_layer;
static void paint_bitmap(void){
 uint8_t *pixels=gbitmap_get_data(s_bitmap);
 uint16_t stride=gbitmap_get_bytes_per_row(s_bitmap);
 for(int y=0;y<24;y++)for(int x=0;x<24;x++)
   pixels[y*stride+x]=((x/4+y/4)%2)?GColorBlack.argb:GColorWhite.argb;
}
static char s_note[84];
static void read_resource(void){
 ResHandle h=resource_get_handle(RESOURCE_ID_FIELD_NOTE);
 size_t len=resource_size(h);
 if(len>=sizeof(s_note))len=sizeof(s_note)-1;
 if(len)resource_load(h,(uint8_t*)s_note,len);
 s_note[len]='\0';
 APP_LOG(APP_LOG_LEVEL_INFO,"Bundled note: %s",s_note);
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
 s_path=gpath_create(&s_path_info);gpath_move_to(s_path,GPoint(b.size.w/2,30));
 s_canvas=layer_create(GRect(0,136,b.size.w,88));
 layer_set_update_proc(s_canvas,draw_canvas);
 layer_add_child(root,s_canvas);
 s_bitmap=gbitmap_create_blank(GSize(24,24),GBitmapFormat8Bit);
 if(s_bitmap){
  paint_bitmap();s_bitmap_layer=bitmap_layer_create(GRect(b.size.w-28,136,24,24));
  bitmap_layer_set_bitmap(s_bitmap_layer,s_bitmap);
  layer_add_child(root,bitmap_layer_get_layer(s_bitmap_layer));
 }
 read_resource();
}
static void unload(Window *w){
 (void)w;
 if(s_bitmap_layer)bitmap_layer_destroy(s_bitmap_layer);if(s_bitmap)gbitmap_destroy(s_bitmap);
 gpath_destroy(s_path);
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
