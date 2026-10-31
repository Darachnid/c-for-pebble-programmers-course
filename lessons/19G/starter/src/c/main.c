#include <pebble.h>
#include "course_display.h"
typedef enum { MODE_VIEW=0, MODE_EDIT=1, MODE_HELP=2 } AppMode;
typedef struct {AppMode mode; int score; bool active;} AppState;
static AppState s_state={MODE_VIEW,0,true};
static Window *s_window; static TextLayer *s_label; static char s_buf[64];
static const char *mode_name(AppMode m) {
 switch(m) {case MODE_VIEW:return "VIEW";case MODE_EDIT:return "EDIT";
            case MODE_HELP:return "HELP";default:return "UNKNOWN";}
}
static void refresh(void) {
 snprintf(s_buf,sizeof(s_buf),"%s: %d",mode_name(s_state.mode),s_state.score);
 text_layer_set_text(s_label,s_buf);
}
static void up_click(ClickRecognizerRef r,void *c) {
 (void)r;(void)c;
 s_state.mode=(AppMode)((s_state.mode+1)%3); refresh();
}
static void down_click(ClickRecognizerRef r,void *c) {
 (void)r;(void)c;
 s_state.score++; refresh();
}
static void click_config(void *c) {
 (void)c;window_single_click_subscribe(BUTTON_ID_UP,up_click);
 window_single_click_subscribe(BUTTON_ID_DOWN,down_click);
}
static void on_load(Window *w) {
 GRect b=layer_get_bounds(window_get_root_layer(w));
 GRect safe=course_content_rect(b);
 s_label=text_layer_create(GRect(safe.origin.x,safe.origin.y+(safe.size.h-65)/2,safe.size.w,65));
 text_layer_set_font(s_label,fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
 text_layer_set_text_alignment(s_label,GTextAlignmentCenter);
 layer_add_child(window_get_root_layer(w),text_layer_get_layer(s_label));
 refresh();
}
static void on_unload(Window *w) {(void)w;text_layer_destroy(s_label);}
static void init(void) {
 s_window=window_create(); window_set_click_config_provider(s_window,click_config);
 window_set_window_handlers(s_window,(WindowHandlers){.load=on_load,.unload=on_unload});
 window_stack_push(s_window,true);
}
static void deinit(void){window_destroy(s_window);}
int main(void){init();app_event_loop();deinit();}
