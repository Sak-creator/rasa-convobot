






#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#class GenerateSQLQueryAction(Action):
  
 #   def name(self) -> Text:
  #      return "generate_sql_query_action"

   # def run(self, dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
     #       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
      #  dispatcher.utter_message(Text='done')
       # entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #print(tracker.latest_message)
        #if intent == "provide_table":
         #    sql_query = f"SELECT * FROM {table}"
          #   dispatcher.utter_message(template="utter_display_results", query=sql_query)
        #else:
         #    sql_query = "default"

       # return []



      #  class GenerateWHEREQueryAction(Action):
  
    #def name(self) -> Text:
       # return "generate_where_query_action"

    #def run(self, dispatcher: CollectingDispatcher,
           # tracker: Tracker,
            #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
       # dispatcher.utter_message(Text='done')
        #entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #operator = tracker.get_slot("operator")
        #value = tracker.get_slot("value")
        #column = tracker.get_slot("column")
        #print(tracker.latest_message)
        #if intent == "provide_table_where":
            # where_query = f"SELECT * FROM {table} WHERE {column} {operator} {value}  ;"
             #dispatcher.utter_message(template="utter_display_where", where=where_query)
        #else:
         #    sql_query = "default"

#        return []
#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#class GenerateSQLQueryAction(Action):
 #   def name(self) -> Text:
  #      return "generate_sql_query_action"

   # def run(self, dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
     #       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
      #  table = tracker.get_slot("table")
       # namee = tracker.get_slot("namee")
        #experience = tracker.get_slot("experience")
        #location = tracker.get_slot("location")
    
        #sql_query = f"SELECT * FROM {table} WHERE location = '{location}' AND experience = {experience} AND name = '{namee}'"
            
        #dispatcher.utter_message(template="utter_display_results", query=sql_query)

        #return []



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



class CollectInformationAction(Action):
    def name(self) -> Text:
        return "action_collect_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve the slot values
        namee = tracker.get_slot("namee")
        location = tracker.get_slot("location")
        experience = tracker.get_slot("experience")
        table = tracker.get_slot("table")

        # Check if all slots have been filled
        if namee and location and experience and table:
            response = f"SELECT * FROM {table} WHERE location = '{location}' AND experience = '{experience}' AND name = '{namee}'"
        elif not table:
            response = "Please provide the name of the table you want to create a record in:"
        elif not namee:
            response = "Please provide your name:"
        elif not experience:
            response = "Please provide experience:"
        elif not location:
            response = "Please provide your location:"
        else:
            response = "Something went wrong. Please try again."

        dispatcher.utter_message(text=response)

        

        return []


