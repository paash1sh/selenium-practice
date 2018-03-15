# my selenium learning notes

## things i learned

- find_element_by_id is the easiest way to find elements
- always add time.sleep() otherwise selenium is too fast
- find_element_by_css_selector is more flexible than by_id
- Chrome needs chromedriver installed separately (had trouble with this at first)
- driver.quit() is important otherwise chrome stays open

## errors i got and how i fixed them

- NoSuchElementException - element not found, had to check the id/class name again
- ElementNotInteractableException - element was there but couldnt click, used time.sleep to wait
- SessionNotCreatedException - chromedriver version didnt match chrome version, had to download right version

## next things to learn
- how to take screenshots on failure
- implicit and explicit waits (better than time.sleep)
- page object model
- how to run tests without opening browser (headless)

## resources
- https://selenium-python.readthedocs.io
- https://the-internet.herokuapp.com (good practice site)
# notes
# notes update
