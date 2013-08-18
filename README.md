opentrack
=========

Use OpenStreetMaps Android app to log own GPS tracks.

https://play.google.com/store/apps/details?id=net.osmand

As of 19 August 2013, the application can log waypoints sent over by
OsmAnd application and display them in Admin site.

### Installation

This app is tweaked to easily run on Heroku, so you might want to try that.
All you need to do is follow Heroku's getting started documents and do a
`git push heroku master` to deploy the code. If you want to store large
amounts of data, please pick a database plan.

There is no security - so if someone knows your app URL, it is possible
to inject fake or useless data at this point. This will be addressed with
a preset key in settings file that must be passed along to verify data.

### Why?

This app can form the base framework to play with your live location data.
Perhaps your app can monitor your location and send you reminders, or if
you live in another city and visit parents often, the app could send them
a heads up when you are expected to be home in next hour. It's entirely up
to you at this point.

### I just want a dump/gpx/kml… alternatives?

Since this app is made for OpenStreetMaps Android app, I'll suggest another
Android app: look into https://github.com/mendhak/gpslogger which is available
on Play Store at: https://play.google.com/store/apps/details?id=com.mendhak.gpslogger