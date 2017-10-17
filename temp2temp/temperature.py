#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Celsius:
    """ Collection of temperature conversions from Celsius """

    @staticmethod
    def to_delisle(celsius):
        """ Convert celsius to delisle """
        return (100 - celsius) * 3 / 2

    @staticmethod
    def to_fahrenheit(celsius):
        """ Convert celsius to fahrenheit """
        return celsius * 9 / 5 + 32

    @staticmethod
    def to_kelvin(celsius):
        """ Convert celsius to kelvin """
        return celsius + 273.15

    @staticmethod
    def to_newton(celsius):
        """ Convert celsius to newton """
        return celsius * 33 / 100

    @staticmethod
    def to_rankine(celsius):
        """ Convert celsius to rankie """
        return (celsius + 273.15) * 9 / 5

    @staticmethod
    def to_reaumur(celsius):
        """ Convert celsius to reaumur """
        return celsius * 4 / 5

    @staticmethod
    def to_romer(celsius):
        """ Convert celsius to romer """
        return celsius * 21 / 40 + 7.5


class Delisle:
    """ Collection of temperature conversions from Delisle """

    @staticmethod
    def to_celsius(delisle):
        """ Convert delisle to celsius """
        return 100 - delisle * 2 / 3

    @staticmethod
    def to_fahrenheit(delisle):
        """ Convert delisle to fahrenheit """
        return 212 - delisle * 6 / 5

    @staticmethod
    def to_kelvin(delisle):
        """ Convert delisle to kelvin """
        return 373.15 - (delisle * 2 / 3)

    @staticmethod
    def to_newton(delisle):
        """ Convert delisle to newton """
        return 33 - delisle * 11 / 50

    @staticmethod
    def to_rankine(delisle):
        """ Convert delisle to rankine """
        return 671.67 - delisle * 6 / 5

    @staticmethod
    def to_reaumur(delisle):
        """ Convert delisle to reaumur """
        return 80 - delisle * 8 / 15

    @staticmethod
    def to_romer(delisle):
        """ Convert delisle to romer """
        return 60 - delisle * 7 / 20


class Fahrenheit:
    """ Collection of temperature conversions from Fahrenheit """

    @staticmethod
    def to_celsius(fahrenheit):
        """ Convert fahrenheit to celsius """
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def to_delisle(fahrenheit):
        """ Convert fahrenheit to delisle """
        return (212 - fahrenheit) * 5 / 6

    @staticmethod
    def to_kelvin(fahrenheit):
        """ Convert fahrenheit to kelvin """
        return (fahrenheit + 459.67) * 5 / 9

    @staticmethod
    def to_newton(fahrenheit):
        """ Convert fahrenheit to newton """
        return (fahrenheit - 32) * 11 / 60

    @staticmethod
    def to_rankine(fahrenheit):
        """ Convert fahrenheit to rankine """
        return fahrenheit + 459.67

    @staticmethod
    def to_reaumur(fahrenheit):
        """ Convert fahrenheit to reaumur """
        return (fahrenheit - 32) * 4 / 9

    @staticmethod
    def to_romer(fahrenheit):
        """ Convert fahrenheit to romer """
        return (fahrenheit - 32) * (7 / 24) + 7.5


class Kelvin:
    """ Collection of temperature conversions from Kelvin """

    @staticmethod
    def to_celsius(kelvin):
        """ Convert kelvin to celsius """
        return kelvin - 273.15

    @staticmethod
    def to_delisle(kelvin):
        """ Convert kelvin to delisle """
        return (373.15 - kelvin) * 3 / 2

    @staticmethod
    def to_fahrenheit(kelvin):
        """ Convert kelvin to fahrenheit """
        return (kelvin * 9 / 5) - 459.67

    @staticmethod
    def to_newton(kelvin):
        """ Convert kelvin to newton """
        return (kelvin - 273.15) * 33 / 100

    @staticmethod
    def to_rankine(kelvin):
        """ Convert kelvin to rankine """
        return kelvin * 9/5

    @staticmethod
    def to_reaumur(kelvin):
        """ Convert kelvin to reaumur """
        return (kelvin - 273.15) * 4 / 5

    @staticmethod
    def to_romer(kelvin):
        """ Convert kelvin to romer """
        return (kelvin - 273.15) * (21 / 40) + 7.5


class Rankine:
    """ Collection of temperature conversions from Rankine """

    @staticmethod
    def to_celsius(rankine):
        """ Convert rankine to celsius """
        return (rankine - 491.67) * 5 / 9

    @staticmethod
    def to_delisle(rankine):
        """ Convert rankine to delisle """
        return (671.67 - rankine) * 5 / 6

    @staticmethod
    def to_fahrenheit(rankine):
        """ Convert rankine to fahrenheit """
        return rankine - 459.67

    @staticmethod
    def to_kelvin(rankine):
        """ Convert rankine to kelvin """
        return rankine * 5 / 9

    @staticmethod
    def to_newton(rankine):
        """ Convert rankine to newton """
        return (rankine - 491.67) * 11 / 60

    @staticmethod
    def to_reaumur(rankine):
        """ Convert rankine to reaumur """
        return (rankine - 491.67) * 4 / 9

    @staticmethod
    def to_romer(rankine):
        """ Convert rankine to romer """
        return (rankine - 491.67) * (7 / 24) + 7.5


class Reaumur:
    """ Collection of temperature conversions from Reaumur """

    @staticmethod
    def to_celsius(reaumur):
        """ Convert reaumur to celsius """
        return reaumur * 5 / 4

    @staticmethod
    def to_delisle(reaumur):
        """ Convert reaumur to delisle """
        return (80 - reaumur) * 15 / 8

    @staticmethod
    def to_fahrenheit(reaumur):
        """ Convert reaumur to fahrenheit """
        return reaumur * 9 / 4 + 32

    @staticmethod
    def to_kelvin(reaumur):
        """ Convert reaumur to kelvin """
        return reaumur * 5 / 4 + 273.15

    @staticmethod
    def to_newton(reaumur):
        """ Convert reaumur to newton """
        return reaumur * 33 / 80

    @staticmethod
    def to_rankine(reaumur):
        """ Convert reaumur to rankine """
        return reaumur * 9 / 4 + 491.67

    @staticmethod
    def to_romer(reaumur):
        """ Convert reaumur to romer """
        return reaumur * (21 / 32) + 7.5


class Newton:
    """ Collection of temperature conversions from Newton """

    @staticmethod
    def to_celsius(newton):
        """ Convert newton to celsius """
        return newton * 100 / 33

    @staticmethod
    def to_delisle(newton):
        """ Convert newton to delisle """
        return (33 - newton) * 50 / 11

    @staticmethod
    def to_fahrenheit(newton):
        """ Convert newton to fahrenheit """
        return newton * 60 / 11 + 32

    @staticmethod
    def to_kelvin(newton):
        """ Convert newton to kelvin """
        return newton * 100 / 33 + 273.15

    @staticmethod
    def to_rankine(newton):
        """ Convert newton to rankine """
        return newton * 60 / 11 + 491.67

    @staticmethod
    def to_reaumur(newton):
        """ Convert newton to reaumur """
        return newton * 80 / 33

    @staticmethod
    def to_romer(newton):
        """ Convert newton to romer """
        return newton * 35 / 22 + 7.5


class Romer:
    """ Collection of temperature conversions from Romer """

    @staticmethod
    def to_celsius(romer):
        """ Convert romer to celsius """
        return (romer - 7.5) * 40 / 21

    @staticmethod
    def to_delisle(romer):
        """ Convert romer to delisle """
        return (60 - romer) * 20 / 7

    @staticmethod
    def to_fahrenheit(romer):
        """ Convert romer to fahrenheit """
        return (romer - 7.5) * 24 / 7 + 32

    @staticmethod
    def to_kelvin(romer):
        """ Convert romer to kelvin """
        return (romer - 7.5) * 40 / 21 + 273.15

    @staticmethod
    def to_newton(romer):
        """ Convert romer to newton """
        return (romer - 7.5) * 22 / 35

    @staticmethod
    def to_rankine(romer):
        """ Convert romer to rankine """
        return (romer - 7.5) * 24 / 7 + 491.67

    @staticmethod
    def to_reaumur(romer):
        """ Convert romer to reaumur """
        return (romer - 7.5) * 32 / 21
