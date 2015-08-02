<?php
    include_once "config/parse.config.php";
    include_once "lib/php/vendor/autoload.php";

    use Parse\ParseObject;
    #use Parse\ParseQuery;
    #use Parse\ParseACL;
    #use Parse\ParsePush;
    #use Parse\ParseUser;
    #use Parse\ParseInstallation;
    #use Parse\ParseException;
    #use Parse\ParseAnalytics;
    #use Parse\ParseFile;
    #use Parse\ParseCloud;
    use Parse\ParseClient;

    ParseClient::initialize($PARSE_APP_ID, $PARSE_REST_KEY, $PARSE_MASTER_KEY);

    $testObject = ParseObject::create("TestObject");
    $testObject->set("foo", "bar");
    $testObject->save();


