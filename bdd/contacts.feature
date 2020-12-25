Scenario Outline: Add new contact
Given a contact list
Given a contact with <firstname> and <lastname>
When I add the contact to the list
Then the new contact list is equal to the old list with the added contact

Examples:
| firstname  | lastname  |
| firstname1 | lastname1 |

Scenario Outline: Delete contact
Given a non-empty contact list
Given a random contact from the list
When I delete the contact from the list
Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Modify contact
Given a non-empty contact list
Given a random contact from the list
When I modify the contact with <firstname> and <lastname>
Then the new contact list is equal to the old list with the modified contact

Examples:
| firstname  | lastname    |
| Fedor      | Emelyanenko |