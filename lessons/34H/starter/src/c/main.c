#include <pebble.h>
#include "course_display.h"
/* Field Instrument B1: use hardware to corroborate emulator traces. */
static Window *s_window;static TextLayer *s_title,*s_data;
static char s_text[100];
static time_t s_last_accel_draw = 0;static int s_x,s_y,s_z,s_heading=-1;
static void show(void){
 snprintf(s_text,sizeof(s_text),"X %d\nY %d\nZ %d",s_x,s_y,s_z);
 text_layer_set_text(s_data,s_text);
}
static void acceleration(AccelData *data,uint32_t count){
 if(!count)return;
 s_x=data[count-1].x;s_y=data[count-1].y;s_z=data[count-1].z;
 /* Keep newest sample; at most one accelerometer-driven redraw per second. */
 time_t now = time(NULL);
 if(now != s_last_accel_draw) {
   s_last_accel_draw = now;
   show();
 }
}


static void load(Window *w){
 Layer *root=window_get_root_layer(w);GRect b=layer_get_bounds(root);
 GRect safe=course_content_rect(b);
 s_title=text_layer_create(GRect(safe.origin.x, safe.origin.y+3,
     safe.size.w, 36));
 s_data=text_layer_create(GRect(safe.origin.x, safe.origin.y+46,
     safe.size.w, safe.size.h-46));
 text_layer_set_text(s_title,"FIELD INSTRUMENT");
 text_layer_set_font(s_title,fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
 text_layer_set_text(s_data,"Waiting for accelerometer...");
 layer_add_child(root,text_layer_get_layer(s_title));
 layer_add_child(root,text_layer_get_layer(s_data));
}
static void unload(Window *w){(void)w;text_layer_destroy(s_data);text_layer_destroy(s_title);}
static void init(void){
 s_window=window_create();window_set_window_handlers(s_window,(WindowHandlers){.load=load,.unload=unload});
 
 window_stack_push(s_window,true);
 accel_data_service_subscribe(10,acceleration);accel_service_set_sampling_rate(ACCEL_SAMPLING_10HZ);
 
}
static void deinit(void){
 
 accel_data_service_unsubscribe();
 window_destroy(s_window);
}
int main(void){init();app_event_loop();deinit();}
