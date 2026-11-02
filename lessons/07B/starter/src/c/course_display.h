#ifndef COURSE_DISPLAY_H
#define COURSE_DISPLAY_H
#include <pebble.h>
/* One conservative, centered content region for both Pebble Time 2 and
 * Pebble Round 2. A square inscribed in the round screen prevents clipped
 * titles, counters and controls at the outer edges. */
static GRect course_content_rect(GRect bounds) {
#ifdef PBL_ROUND
  int16_t side = bounds.size.w < bounds.size.h ? bounds.size.w : bounds.size.h;
  int16_t content = (side * 7) / 10;
  return GRect((bounds.size.w - content) / 2,
               (bounds.size.h - content) / 2, content, content);
#else
  return GRect(8, 8, bounds.size.w - 16, bounds.size.h - 16);
#endif
}
#endif
