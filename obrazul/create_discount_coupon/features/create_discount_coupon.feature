Feature: Creating a discount coupon.

    Scenario: When no user is logged in
        Given The user is on the home website page
        And Click on 'Entre'
        When The user logs in
        And The user should be redirected to their dashboard

    Scenario: When is a user logged in
        Given The user is on dashboard page
        Then The user should be click on 'Cupons de Desconto'
        And The user should be redirected to discount coupon creation page

    Scenario: When the user is discount coupon creation page
        Given The user is discount coupon creation page
        Then click on 'Novo Cupom'
        And insert coupon information
        Then click on 'Criar'
