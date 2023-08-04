#include QMK_KEYBOARD_H

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /*
     * ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
     * │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │
     * ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
     * │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │
     * ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
     * │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │
     * ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
     * │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │
     * ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
     * │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │
     * └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
     */
    [0] = LAYOUT_ortho_5x12(
        KC_A,       KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    KC_6,     KC_NO,    KC_NO,     KC_NO,    KC_NO,    KC_NO,
        KC_TAB,     KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,    KC_Y,     KC_NO,    KC_NO,     KC_NO,    KC_NO,    KC_NO,
        KC_ESC,     KC_A,    KC_S,    KC_D,    KC_F,    KC_G,    KC_H,     KC_NO,    KC_NO,     KC_NO,    KC_NO,    KC_NO,
        KC_LSFT,    KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_N,     KC_NO,    KC_NO,     KC_NO,    KC_NO,    KC_NO,
        KC_LCTRL,   KC_LGUI, KC_LALT, KC_D,    KC_SPC,  KC_SPC,  KC_F20,   KC_NO,    KC_NO,     KC_NO,    KC_NO,    KC_NO
    )
};
