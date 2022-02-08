# Created by joset at 2/7/22
Feature: GitHub API Validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credential
    When I hit getRepo API of github
    Then status code of response should be 200