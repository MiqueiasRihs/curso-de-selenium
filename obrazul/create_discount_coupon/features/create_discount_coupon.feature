Feature: Creating a discount coupon.

    Scenario: When no user is logged in
        Given The user is on the home website page
        Then Click on 'Entre'
        Then The user logs in

    Scenario: When is a user logged in
        Given The user is on dashboard page
        Then click on 'Cupons de Desconto'

    Scenario: When the user is discount coupon creation page
        Given The user is discount coupon creation page
        Then insert coupon information
        Then click on 'Criar'
