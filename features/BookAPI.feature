# Created by shivamsoni at 06/01/23
Feature: Test Books APIs
  Test create, get, update & delete APIs

  @get_token
  Scenario Outline: Verify token generation
    Given Credentials <username> and <password> to get auth token
    When I call CreateToken POST API method
    Then response is 200 and token is received
    Examples:
      | username | password    |
      | admin    | password123 |

  @create_booking
  Scenario Outline: Verify create booking
    Given Pass <firstname> and <lastname> and <totalprice> and <depositpaid> and <checkin> and <checkout> and <additionalneeds> params
    When CreateBooking POST API is called
    Then Booking is created
    Examples:
      | firstname   | lastname   | totalprice | depositpaid | checkin    | checkout   | additionalneeds   |
      | shivam      |soni        |   1000     |     True    | 2011-01-01 |2012-01-01  | nothing   |