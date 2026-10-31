#include <pebble.h>
#include "course_display.h"
/* Clock Workshop, snapshot A2. Prior stages are included; extend this one. */
static Window *s_main, *s_detail;
static TextLayer *s_time, *s_status, *s_detail_text;
static char s_time_buf[12], s_status_buf[48];
static int s_count;

static void refresh(void) {
 time_t now=time(NULL); struct tm *tm_now=localtime(&now);
 strftime(s_time_buf,sizeof(s_time_buf),clock_is_24h_style()?"%H:%M":"%I:%M",tm_now);
 text_layer_set_text(s_time,s_time_buf);
 snprintf(s_status_buf,sizeof(s_status_buf),"Count %d",s_count);
 text_layer_set_text(s_status,s_status_buf);
}
static void tick(struct tm *t,TimeUnits u){(void)t;(void)u;refresh();}

static void up(ClickRecognizerRef r,void *c){(void)r;(void)c;if(s_count<99)++s_count;refresh();}
static void down(ClickRecognizerRef r,void *c){(void)r;(void)c;if(s_count>0)--s_count;refresh();}
static void select(ClickRecognizerRef r,void *c){(void)r;(void)c;window_stack_push(s_detail,true);}
static void clicks(void *c){(void)c;
 window_single_click_subscribe(BUTTON_ID_UP,up);
 window_single_click_subscribe(BUTTON_ID_DOWN,down);
 window_single_click_subscribe(BUTTON_ID_SELECT,select);
}
static void load_main(Window *w){
 Layer *root=window_get_root_layer(w); GRect b=layer_get_bounds(root);
 GRect safe=course_content_rect(b);
 s_time=text_layer_create(GRect(safe.origin.x,
     safe.origin.y + safe.size.h/5, safe.size.w, 65));
 s_status=text_layer_create(GRect(safe.origin.x,
     safe.origin.y + (safe.size.h*3)/4, safe.size.w, 36));
 text_layer_set_text_alignment(s_time,GTextAlignmentCenter);
 text_layer_set_text_alignment(s_status,GTextAlignmentCenter);
 text_layer_set_font(s_time,fonts_get_system_font(FONT_KEY_BITHAM_42_BOLD));
 layer_add_child(root,text_layer_get_layer(s_time));
 layer_add_child(root,text_layer_get_layer(s_status));refresh();
}
static void unload_main(Window *w){(void)w;text_layer_destroy(s_status);text_layer_destroy(s_time);}
static void load_detail(Window *w){
 GRect b=layer_get_bounds(window_get_root_layer(w));
 GRect safe=course_content_rect(b);
 s_detail_text=text_layer_create(GRect(safe.origin.x,
     safe.origin.y + (safe.size.h-80)/2, safe.size.w, 80));
 text_layer_set_text(s_detail_text,"Clock details\nBack to return");
 text_layer_set_text_alignment(s_detail_text,GTextAlignmentCenter);
 layer_add_child(window_get_root_layer(w),text_layer_get_layer(s_detail_text));
}
static void unload_detail(Window *w){(void)w;text_layer_destroy(s_detail_text);}
static void init(void){
 s_main=window_create();s_detail=window_create();
 window_set_window_handlers(s_main,(WindowHandlers){.load=load_main,.unload=unload_main});
 window_set_window_handlers(s_detail,(WindowHandlers){.load=load_detail,.unload=unload_detail});
 window_set_click_config_provider(s_main,clicks);
 window_stack_push(s_main,true);
 tick_timer_service_subscribe(MINUTE_UNIT,tick);
 
}
static void deinit(void){
 
 tick_timer_service_unsubscribe();window_destroy(s_detail);window_destroy(s_main);
}
int main(void){init();app_event_loop();deinit();}
