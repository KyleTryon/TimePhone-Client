from services.callRoutines.routine_emergency import RoutineEmergency
from services.callRoutines.routine_operator import RoutineOperator
from services.callRoutines.routine_traffic import RoutineTraffic
class CallService:
    def __init__(self):
        self.phone_book = {
          '411': {
            'name': 'Operator',
            'call': RoutineOperator
          },
          '#' : {
            'name': 'Operator',
            'call': RoutineOperator
          },
          '511': {
            'name': 'Traffic and Weather',
            'call': RoutineTraffic
          },
          '911': {
            'name': 'Emergency Services',
            'call': RoutineEmergency
          },
        }
        self.dial_tone = [350, 450]
        # Describe the state of the call service
        self.is_connected = False
    
    def _call(self, call_routine):
        self.is_connected = True
        call_routine()
        self.is_connected = False

    def dial(self, number):
        # If the number is in the phone book, call it
        print('Dialing: ' + number)
        if number in self.phone_book:
            self.phone_book[number]['call']()
            self.is_connected = True
        # If the number is not in the phone book, play a busy signal
        else:
            print('Busy Signal!')

