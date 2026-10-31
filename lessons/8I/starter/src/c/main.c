#include <pebble.h>
/* Field Instrument B2: use hardware to corroborate emulator traces. */
static Window *s_window;static TextLayer *s_title,*s_data;
static char s_text[100];static int s_x,s_y,s_z,s_heading=-1;
static void show(void){
 snprintf(s_text,sizeof(s_text),"X %d\nY %d\nZ %d\nHeading %d",s_x,s_y,s_z,s_heading);
 text_layer_set_text(s_data,s_text);
}
static void acceleration(AccelData *data,uint32_t count){
 if(!count)return;
 s_x=data[count-1].x;s_y=data[count-1].y;s_z=data[count-1].z;show();
}
#ifdef PBL_COMPASS
static void heading(CompassHeadingData d){
 if(d.compass_status==CompassStatusUnavailable||d.compass_status==CompassStatusDataInvalid)
   s_heading=-1;
 else s_heading=TRIGANGLE_TO_DEG(TRIG_MAX_ANGLE-d.magnetic_heading)%360;
 show();
}
#endif

static void load(Window *w){
 Layer *root=window_get_root_layer(w);GRect b=layer_get_bounds(root);
 s_title=text_layer_create(GRect(8,20,b.size.w-16,45));
 s_data=text_layer_create(GRect(8,75,b.size.w-16,130));
 text_layer_set_text(s_title,"FIELD INSTRUMENT");
 text_layer_set_font(s_title,fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
 text_layer_set_text(s_data,"Calibrate by moving the watch.");
 layer_add_child(root,text_layer_get_layer(s_title));
 layer_add_child(root,text_layer_get_layer(s_data));
}
static void unload(Window *w){(void)w;text_layer_destroy(s_data);text_layer_destroy(s_title);}
static void init(void){
 s_window=window_create();window_set_window_handlers(s_window,(WindowHandlers){.load=load,.unload=unload});
 
 window_stack_push(s_window,true);
 accel_data_service_subscribe(10,acceleration);accel_service_set_sampling_rate(ACCEL_SAMPLING_10HZ);
 #ifdef PBL_COMPASS
 compass_service_set_heading_filter(DEG_TO_TRIGANGLE(10));
 compass_service_subscribe(heading);
#endif
}
static void deinit(void){
 #ifdef PBL_COMPASS
 compass_service_unsubscribe();
#endif
 accel_data_service_unsubscribe();
 window_destroy(s_window);
}
int main(void){init();app_event_loop();deinit();}
