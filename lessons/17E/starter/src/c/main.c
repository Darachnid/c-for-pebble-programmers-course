#include <pebble.h>
#define ITEM_COUNT 4
static const char *s_words[ITEM_COUNT]={"BIRDS","FISH","TREES","CLOUDS"};
static int s_selected=0;
static char s_display[64];
static Window *s_window;
static TextLayer *s_label;
static void refresh(void) {
  snprintf(s_display,sizeof(s_display),"%d/%d: %s",
           s_selected+1,ITEM_COUNT,s_words[s_selected]);
  text_layer_set_text(s_label,s_display);
}
static void up_click(ClickRecognizerRef r,void *c) {
  (void)r;(void)c;
  s_selected=(s_selected+1)%ITEM_COUNT;
  refresh();
}
static void down_click(ClickRecognizerRef r,void *c) {
  (void)r;(void)c;
  s_selected=(s_selected+ITEM_COUNT-1)%ITEM_COUNT;
  refresh();
}
static void click_config(void *c) {
  (void)c;
  window_single_click_subscribe(BUTTON_ID_UP,up_click);
  window_single_click_subscribe(BUTTON_ID_DOWN,down_click);
}
static void on_load(Window *w) {
  GRect b=layer_get_bounds(window_get_root_layer(w));
  s_label=text_layer_create(GRect(10,85,b.size.w-20,60));
  text_layer_set_text_alignment(s_label,GTextAlignmentCenter);
  text_layer_set_font(s_label,fonts_get_system_font(FONT_KEY_GOTHIC_24_BOLD));
  layer_add_child(window_get_root_layer(w),text_layer_get_layer(s_label));
  refresh();
}
static void on_unload(Window *w) {(void)w;text_layer_destroy(s_label);}
static void init(void) {
  s_window=window_create();
  window_set_click_config_provider(s_window,click_config);
  window_set_window_handlers(s_window,(WindowHandlers){.load=on_load,.unload=on_unload});
  window_stack_push(s_window,true);
}
static void deinit(void){window_destroy(s_window);}
int main(void){init();app_event_loop();deinit();}
