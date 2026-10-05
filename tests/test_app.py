from streamlit.testing.v1 import AppTest


def start_app(difficulty="Normal"):
    at = AppTest.from_file("../app.py").run()
    if difficulty != "Normal":
        at.selectbox[0].set_value(difficulty).run()
    return at


def test_prompt_shows_range_for_difficulty():
    at = start_app("Hard")
    assert "between 1 and 50" in at.info[0].value


def test_new_game_secret_stays_in_range():
    # the old new game button always picked 1-100, even on Hard
    at = start_app("Hard")
    for _ in range(30):
        at.button[1].click().run()
        assert 1 <= at.session_state.secret <= 50


def test_switching_difficulty_picks_new_secret_in_range():
    at = start_app("Normal")
    at.session_state.secret = 80
    at.selectbox[0].set_value("Easy").run()
    assert 1 <= at.session_state.secret <= 20


def test_new_game_after_win_lets_you_play_again():
    at = start_app("Normal")
    at.session_state.secret = 50
    at.text_input[0].set_value("50")
    at.button[0].click().run()
    assert at.session_state.status == "won"
    at.button[1].click().run()
    assert at.session_state.status == "playing"
