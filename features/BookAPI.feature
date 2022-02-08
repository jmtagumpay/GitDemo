# Created by joset at 2/4/22
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook Post API method
    Then book is successfully added
    And status code of response should be 200

  @library
  # Parameterized Inputs using Example Outline
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook Post API method
    Then book is successfully added
    Examples:
      |isbn    |aisle  |
      |sampleA |12345  |
      |sampleB |67890  |