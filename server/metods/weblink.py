import webbrowser


def weblink(http):
    try:
        webbrowser.open(http, new=0)
    except Exception as e:
        print(f"An error occurred: {e}")


