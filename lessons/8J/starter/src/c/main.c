#include <pebble.h>
/* Field Instrument B3: use hardware to corroborate emulator traces. */
static Window *s_window;static TextLayer *s_title,*s_data;
static char s_text[100];
static time_t s_last_accel_draw = 0;
static const char *s_compass_state = "Unavailable";static int s_x,s_y,s_z,s_heading=-1;
static const char *s_compass_status="Unavailable";
static void show(void){
 if(s_heading >= 0)
    snprintf(s_text,sizeof(s_text),"XYZ %d %d %d\nCompass: %s\nHeading: %d",
             s_x,s_y,s_z,s_compass_state,s_heading);
 else
    snprintf(s_text,sizeof(s_text),"XYZ %d %d %d\nCompass: %s\nHeading: --",
             s_x,s_y,s_z,s_compass_state);
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
#ifdef PBL_COMPASS
static void heading(CompassHeadingData d){
 /* Compass status from completed 8H; distinguish usable-but-calibrating data. */
 switch(d.compass_status) {
   case CompassStatusUnavailable:
     s_compass_state="Unavailable"; s_heading=-1; break;
   case CompassStatusDataInvalid:
     s_compass_state="Calibrating (invalid)"; s_heading=-1; break;
   case CompassStatusCalibrating:
     s_compass_state="Calibrating";
     s_heading=TRIGANGLE_TO_DEG(TRIG_MAX_ANGLE-d.magnetic_heading)%360; break;
   case CompassStatusCalibrated:
     s_compass_state="Valid";
     s_heading=TRIGANGLE_TO_DEG(TRIG_MAX_ANGLE-d.magnetic_heading)%360; break;
   default:
     s_compass_state="Unknown"; s_heading=-1; break;
 }
 show();
}
#endif
static void on_up(ClickRecognizerRef r,void *c){
 (void)r;(void)c;light_enable_interaction();
}
static void clicks(void *c){(void)c;window_single_click_subscribe(BUTTON_ID_UP,on_up);}
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
 window_set_click_config_provider(s_window,clicks);
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
