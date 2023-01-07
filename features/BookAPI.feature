# Created by shivamsoni at 06/01/23
Feature: Test Books APIs
  Test create, get, update & delete APIs

  Scenario Outline: Verify token generation
    Given Credentials <username> and <password> to get auth token
    When I call CreateToken POST API method
    Then response is 200 and token is received
    Examples:
      | username | password    |
      | admin    | password123 |

  Scenario Outline: Verify create booking
    Given Pass <firstname> and <lastname> and <totalprice> and <depositpaid> and <checkin> and <checkout> and <additionalneeds> params
    When CreateBooking POST API is called
    Then Booking is created
    Examples:
      | firstname   | lastname   | totalprice | depositpaid | checkin    | checkout   | additionalneeds   |
      | shivam      |soni        |   1000     |     True    | 2011-01-01 |2012-01-01  | nothing   |



  Scenario: Verify get booking
    Given Pass booking id
    When GetBooking API is called
    Then Booking is returned


Scenario Outline: Verify update booking
    Given Update values of <firstname> and <lastname> and <totalprice> and <depositpaid> and <checkin> and <checkout> and <additionalneeds> params
    When UpdateBooking PUT API is called
    Then Booking is updated
    Examples:
      | firstname   | lastname   | totalprice | depositpaid | checkin    | checkout   | additionalneeds   |
      | yyy      |     xx        |   2000     |     True    | 2013-03-03 |2014-03-03  | something   |


Scenario: Verify delete booking
    Given Pass booking id
    When DeleteBooking API is called
    Then Booking is deleted
    Then I try to call get booking api for deleted booking and verify response is 404 Not Found