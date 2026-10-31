#include <pebble.h>
#include "course_display.h"
#define STORAGE_KEY 19
static Window *s_window;
static TextLayer *s_status;
static int s_count=0;
static int s_minute=0;
static char s_display[64];
static void refresh(void) {
 snprintf(s_display,sizeof(s_display),"count %d  min %02d",s_count,s_minute);
 text_layer_set_text(s_status,s_display);
}
static void up_click(ClickRecognizerRef recognizer,void *context) {
 (void)recognizer;(void)context;
 ++s_count; persist_write_int(STORAGE_KEY,s_count); refresh();
}
static void down_click(ClickRecognizerRef recognizer,void *context) {
 (void)recognizer;(void)context;
 if(s_count>0) --s_count;
 persist_write_int(STORAGE_KEY,s_count); refresh();
}
static void click_config(void *context) {
 (void)context;
 window_single_click_subscribe(BUTTON_ID_UP,up_click);
 window_single_click_subscribe(BUTTON_ID_DOWN,down_click);
}
static void tick_handler(struct tm *tm_now,TimeUnits changed) {
 (void)changed;
 s_minute=tm_now->tm_min; refresh();
}
static void on_load(Window *w) {
 GRect b=layer_get_bounds(window_get_root_layer(w));
 GRect safe=course_content_rect(b);
 s_status=text_layer_create(GRect(safe.origin.x,safe.origin.y+(safe.size.h-75)/2,safe.size.w,75));
 text_layer_set_text_alignment(s_status,GTextAlignmentCenter);
 text_layer_set_font(s_status,fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
 layer_add_child(window_get_root_layer(w),text_layer_get_layer(s_status));
 refresh();
}
static void on_unload(Window *w){(void)w;text_layer_destroy(s_status);}
static void init(void) {
 if(persist_exists(STORAGE_KEY)) s_count=persist_read_int(STORAGE_KEY);
 time_t now=time(NULL);s_minute=localtime(&now)->tm_min;
 s_window=window_create();
 window_set_click_config_provider(s_window,click_config);
 window_set_window_handlers(s_window,(WindowHandlers){.load=on_load,.unload=on_unload});
 window_stack_push(s_window,true);
 tick_timer_service_subscribe(MINUTE_UNIT,tick_handler);
}
static void deinit(void) {
 tick_timer_service_unsubscribe();
 window_destroy(s_window);
}
int main(void){init();app_event_loop();deinit();}
