<?php
    include_once "config/parse.config.php";
    include_once "lib/php/vendor/autoload.php";

    use Parse\ParseObject;
    use Parse\ParseQuery;
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

    /*
    $object = ParseObject::create("TestObject");
    $objectId = $object->getObjectId();
    $php = $object->get("elephant");

    // Set values:
    $object->set("elephant", "php");
    $object->set("today", new DateTime());
    $object->setArray("mylist", [1, 2, 3]);
    $object->setAssociativeArray(
        "languageTypes", array("php" => "awesome", "ruby" => "wtf")
    );
    // Save:
    $object->save();
    */

$query = new ParseQuery("TestObject");

// Get a specific object:
$object = $query->get("zD67yQOxAi");

$query->limit(10); // default 100, max 1000

// Just the first result:
$first = $query->first();

var_dump($first);
