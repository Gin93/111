

"""
COMP3620-6320 Artificial Intelligence 2017 - Planning Assignment Q1
Classes for representing a STRIPS planning task and capturing its semantics

Enter your details below:

Name: Zi　JIN
Student Code: U5541673
email: U5541673@anu.edu.au


Methods to be implemented
- applicable
- apply
- goal_reached
- get_successor_states

Each of these methods requires understanding of the semantics of PDDL planning

"""
import copy

class Action:
	def __init__(self, name, preconditions, add_effects, del_effects):
		self.name = name
		self.preconditions = frozenset(preconditions)
		self.add_effects = frozenset(add_effects)
		self.del_effects = frozenset(del_effects)

	def applicable(self, state):
		"""
		@return True if action is applicable in state,
				False otherwise
		// the preconditions should appear in the state. 
		"""
		#print('--------------')
		for precondition in self.preconditions:
			if precondition not in state:
				return False
		return True 
		# raise NotImplementedError

	def apply(self, state):
		"""
		@param state The state that the action should be applied to
		@return A new state (set of facts) after the application of the
				action
		"""
		tem_state = set()
		for s in state:
			tem_state.add(s)
		
		
		for fact in self.add_effects:
			tem_state.add(fact)
			
		for fact in self.del_effects:
			if fact in tem_state:
				tem_state.remove(fact)
				
		return frozenset (tem_state)


	def __str__(self):
		s = '%s\n' % self.name
		for group, facts in [('PRE', self.preconditions),
							 ('ADD', self.add_effects),
							 ('DEL', self.del_effects)]:
			for fact in facts:
				s += '  %s: %s\n' % (group, fact)
		return s

	def __repr__(self):
		return '<Op %s>' % self.name


class Task:
	"""
	A STRIPS planning task
	"""
	def __init__(self, name, facts, initial_state, goals, actions):
		"""
		@param name The task's name
		@param facts A set of all the fact names that are valid in the domain
		@param initial_state A set of fact names that are true at the beginning
		@param goals A set of fact names that must be true to solve the problem
		@param actions A set of action instances for the domain
		"""
		self.name = name
		self.facts = facts
		self.initial_state = initial_state
		self.goals = goals
		self.actions = actions

	def goal_reached(self, state):
		"""
		@return True if all the goals are reached, False otherwise
		"""
		for goal in self.goals:
			if goal not in state:
				return False 
		return True 
		
		#raise NotImplementedError

	def get_successor_states(self, state):
		""" 为什么不用dic
		@return A list with (op, new_state) pairs where "op" is the applicable
		action and "new_state" the state that results when "op" is applied
		in state "state".
		"""
		successor_states = [];
		for action in self.actions:
			if action.applicable(state):
				successor_states.append ((action, action.apply(state)))
		return successor_states;

		#raise NotImplementedError

	def __str__(self):
		s = 'Task {0}\n  Vars:  {1}\n  Init:  {2}\n  Goals: {3}\n  Ops:   {4}'
		return s.format(self.name, ', '.join(self.facts),
							 self.initial_state, self.goals,
							 '\n'.join(map(repr, self.actions)))

	def __repr__(self):
		string = '<Task {0}, vars: {1}, actions: {2}>'
		return string.format(self.name, len(self.facts), len(self.actions))	
