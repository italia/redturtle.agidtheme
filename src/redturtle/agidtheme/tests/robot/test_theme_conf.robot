
*** Settings *****************************************************************
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/saucelabs.robot
Resource  keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote
Test Setup  Run keywords  Plone Test Setup
Test Teardown  Run keywords  Plone Test Teardown
*** Test Cases ***************************************************************

Scenario: Set parameters in redturtle.agitheme controlpanel
  Given a logged-in Manager
    and the redturtle agid theme control panel
    and I set the Shareable content types
  When I add new Page '${id}' and page is configured in agidtheme controlpanel
  Then in the document page I should see all configuration

*** Variables ***

 ${id}  new-document
 ${title}  New document
 ${followlinks}  facebook|https://www.facebook.com\n\rtwitter|https://www.twitter.com\nyoutube|https://www.youtube.com\nmedium|https://medium.com/\nlinkedin|https://www.linkedin.com/\nstorify|https://storify.com/\nrss|https://news.google.it/?output=rss\nnewsletter|https://developers.google.com/newsletter/
 ${link1title}  Link 1
 ${link1href}  http://link1.com
 ${link2title}  Link 2
 ${link2href}  http://link2.com

*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in manager
  Enable autologin as  Manager

the redturtle agid theme control panel
  Go to  ${PLONE_URL}/@@redturtle-agidtheme-controlpanel

I set the Shareable content types
  Select From List By Label  form.widgets.available_types.from  Page
  Click Button  css=#form-widgets-available_types button[name="from2toButton"]
  Select From List By Label  form.widgets.available_socials.from  Google
  Click Button  css=#form-widgets-available_socials button[name="from2toButton"]
  Input Text  name=form.widgets.follow_us_links  ${followlinks}
  Input Text  name=form.widgets.header_link_label  ${link1title}
  Input Text  name=form.widgets.header_link_url  ${link1href}
  Input Text  name=form.widgets.header_second_link_label  ${link2title}
  Input Text  name=form.widgets.header_second_link_url  ${link2href}
  Click Button  Save
  Wait until page contains  Changes saved


# --- When ---------------------------------------------------------------------

I add new Page '${id}' and page is configured in agidtheme controlpanel
  Go to  ${PLONE_URL}
  Create content  type=Document  id=${id}  title=${title}

# --- Then ----------------------------------------------------------------------

In the document page I should see all configuration
  Go to  ${PLONE_URL}/${id}
  Page should contain element  css=.header-banner-inner .header-banner-owner a[href="${link1href}"]
  Page should contain element  css=.header-banner-inner .header-banner-second-link a[href="${link2href}"]
  Wait For Condition  return $('.header-banner-inner .header-banner-owner a').text() === '${link1title}'
  Wait For Condition  return $('.header-banner-inner .header-banner-second-link a').text() === '${link2title}'
  Page should contain element  css=#portal-header #header-social ul li a[href*="facebook"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="twitter"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="youtube"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="medium"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="linkedin"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="storify"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="rss"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="newsletter"]
  Page should contain element  css=#portal-header #header-social ul li a[href*="facebook"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="twitter"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="youtube"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="medium"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="linkedin"] svg
  # Page should contain element  css=#portal-header #header-social ul li a[href*="storify"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="rss"] svg
  Page should contain element  css=#portal-header #header-social ul li a[href*="newsletter"] svg
  Page should contain element  css=#portal-column-two .share.share-visible
