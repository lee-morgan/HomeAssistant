#--------------------------------------------------------------------------------------------------
# Set the state or other attributes for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
originalState = inputStateObject.state
newState = inputStateObject.state
inputAttributesObject = inputStateObject.attributes.copy()

if originalState == 'not_home': 
    newState = 'home'
elif originalState == 'home': 
    newState = 'not_home'

hass.states.set(inputEntity, newState, inputStateObject.attributes)
hass.states.set(inputEntity, originalState, inputStateObject.attributes)