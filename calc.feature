Feature: Calculator Testing
	Scenario: 9 + 3 testing
	
		When I click 9 button
		And I click plus button
		And I click 3 button
		And I click = button
		Then the result is 13