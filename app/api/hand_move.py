import asyncio
from app.hardware.pin_handler import PinHandler
from app.utils.hand_model import Hand


def hand_handler(instructions):
    # {"engine": "upper_thumb", "value": 0},
    # {"engine": "lower_thumb", "value": 0.5},
    # {"engine": "index_finger", "value": 0.8},
    # {"engine": "middle_finger", "value": 1},
    # {"engine": "ring_finger", "value": 0},
    # {"engine": "pinky_finger", "value": 0}
    # instructions = instructions.split("\n")

    upper_thumb = Hand.upperThumb.value
    lower_thumb = Hand.lowerThumb.value
    index_finger = Hand.indexFinger.value
    middle_finger = Hand.middleFinger.value
    ring_finger = Hand.ringFinger.value

    hand = {
        upper_thumb: 17,
        lower_thumb: 18,
        index_finger: 19,
        middle_finger: 20,
        ring_finger: 21,
    }

    try:
        for i in instructions:
            if i["engine"] == index_finger or i["engine"] == middle_finger:
                gpio_handler = PinHandler(hand[i["engine"]])
                if i["value"] == 0:
                    gpio_handler.set_servo_position(90)

                elif i["value"] == 1:
                    gpio_handler.set_servo_position(0)
                gpio_handler.stop()

            if i["engine"] == ring_finger:
                gpio_handler = PinHandler(hand[i["engine"]])

                if i["value"] == 0:
                    gpio_handler.set_servo_position(170)

                elif i["value"] == 1:
                    gpio_handler.set_servo_position(90)

                gpio_handler.stop()

            if i["engine"] != "pinky_finger":
                gpio_handler = PinHandler(hand[i["engine"]])
                gpio_handler.set_servo_position(parse_data(i["value"]))

                gpio_handler.stop()

    except Exception as e:
        raise e

    # print(instructions)


def parse_data(data):
    max = 89
    print(int(max * data))
    return int(max * data)