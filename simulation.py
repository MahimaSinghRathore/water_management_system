import simpy
import random

def log_event(log, hour, event, usage=0, leak=0, grey=0):
    """Helper function to add an entry to the event log."""
    log.append({
        "time": hour,
        "event": event,
        "usage": usage,
        "leak": leak,
        "grey": grey
    })

def smart_water_simulation(env, log, water_data, peak_hours):
    tank_capacity = 1000
    tank_level = tank_capacity
    leak_probability = 0.1
    greywater_used_total = 0
    leak_counter = 0

    while True:
        hour = env.now % 24
        day = env.now // 24 + 1  # Day tracking if simulation runs longer
        is_peak = hour in peak_hours

        # Water consumption (leak is not part of consumption)
        base_usage = random.randint(20, 40) if is_peak else random.randint(5, 15)

        # Determine if leakage occurs
        leak_occurred = random.random() < leak_probability and leak_counter < 2
        leak_amount = random.randint(10, 20) if leak_occurred else 0
        
        # Log water usage (excluding leak)
        event_msg = f"Day {day}, Hour {hour}: Used {base_usage}L"
        if leak_occurred:
            event_msg += f" | Leak +{leak_amount}L!"
        
        # Log water consumption
        log_event(log, hour, event_msg, usage=base_usage, leak=leak_amount)

        # Update tank level
        tank_level -= base_usage  # Regular consumption
        tank_level -= leak_amount  # Subtract leakage separately
        
        leak_counter += 1 if leak_occurred else 0

        # Handle tank underflow (dry tank)
        if tank_level < 0:
            log_event(log, hour, f"!!! Day {day}, Hour {hour}: Tank dry (underflow) !!!")
            tank_level = 0

        # Refill the tank at 2 AM
        if hour == 2:
            refill = tank_capacity
            tank_level += refill
            log_event(log, hour, f"*** Day {day}, Hour {hour}: Tank refilled +{refill}L ***")

        # Use greywater if water consumption is low during off-peak hours
        if not is_peak and base_usage < 10:
            grey_used = random.randint(5, 10)
            greywater_used_total += grey_used
            log[-1]["grey"] = grey_used  # Add greywater usage to the last event
            log_event(log, hour, f"Greywater used: {grey_used}L", grey=grey_used)

        # Track tank level
        water_data.append(tank_level)

        # Simulate next time step (1 hour)
        yield env.timeout(1)

def run_simulation():
    env = simpy.Environment()
    log = []
    water_data = []
    peak_hours = [6, 7, 8, 19, 20, 21]  # Hostel peak hours
    env.process(smart_water_simulation(env, log, water_data, peak_hours))
    env.run(until=24)  # Simulate for 24 hours (1 day)
    return log, water_data









