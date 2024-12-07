Feature: Unsuccessful Terminate Rent Contract
  Scenarios related to the unsuccessful termination of a rent smart contract.

Background:
Given the landlord Landlord01
  And the tenant Tenant01
  And the tenant address Address01
  And the contract total value 24000
  And the monthly value 2000
  And the months quantity 12

@OneYearPaymentRentContract
Scenario: Terminate a rent contract unsuccessfully if payment is delayed
    And the effective date of the contract 30
    And the creation date 10
    And the contract is created
    And the contract is activated
  When a monthly payment is done on day 120
    Then the contract status must be UnsuccessfulTermination
    And the penalty is 2400
    And the local availability is true

@OneYearPaymentRentContract
Scenario: Terminate a rent contract unsuccessfully if water is not paid
    And the effective date of the contract 30
    And the creation date 10
    And the contract is created
    And the contract is activated
    And a monthly payment is done on day 40
    And a monthly payment is done on day 70
    And a monthly payment is done on day 100
    And a monthly payment is done on day 130
    And a monthly payment is done on day 160
    And a monthly payment is done on day 190
    And a monthly payment is done on day 220
    And a monthly payment is done on day 250
    And a monthly payment is done on day 280
    And a monthly payment is done on day 310
    And a monthly payment is done on day 340
    And taxes payment is done
  When a monthly payment is done on day 370
    Then the contract status must be UnsuccessfulTermination
    And the water paid is false
    And the penalty is 2400
    And the local availability is true

@OneYearPaymentRentContract
Scenario: Terminate a rent contract unsuccessfully if taxes are not paid
    And the effective date of the contract 30
    And the creation date 10
    And the contract is created
    And the contract is activated
    And a monthly payment is done on day 40
    And a monthly payment is done on day 70
    And a monthly payment is done on day 100
    And a monthly payment is done on day 130
    And a monthly payment is done on day 160
    And a monthly payment is done on day 190
    And a monthly payment is done on day 220
    And a monthly payment is done on day 250
    And a monthly payment is done on day 280
    And a monthly payment is done on day 310
    And a monthly payment is done on day 340
    And water payment is done
  When a monthly payment is done on day 370
    Then the contract status must be UnsuccessfulTermination
    And the taxes paid is false
    And the penalty is 2400
    And the local availability is true
