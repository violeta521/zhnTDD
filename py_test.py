from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #(1)
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
         # Edith has heard about a cool new online to-do app .She goed
         #to check out its homepage
         self.browser.get('http://localhost:8000')

         #She notices the page title and header mention to-do lists
         #assert 'To-Do' in browser.title,"Browser title was "+browser.title #(4)
         self.assertIn('To-Do',self.browser.title)
         self.fail('Finish the test')#(5)


         #She is invited to enter a to-do item straight away



         #She tyepes "Buy peacock feathers" into a text box (Edith's hobby
         #is tying fly-fishing lures)

         #when she hits enter,the page updates ,and now the page lists
         #"1: Buy peacock feather" as an item in a to-do list

         #There is still a text box inviting her to add another item.She
         #enters "Use peacock feathers to make a fly"(Edith is very methodical)

         #the page updates again, and now shows both items on her list

         #Edith wonders whether the site will remember her list. Then she sees
         #that the site has generated a unique URL for her -- there is some
         #explanatory text to that effect.

         #She visits that URL - her to-do list is still there.

         #Satisfied, she goes back to sleep


         #browser.quit()

if __name__=='__main__':
    unittest.main(warnings='ignore')

