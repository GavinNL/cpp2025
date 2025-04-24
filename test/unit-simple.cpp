#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>

int func(int y)
{
    return y+4;
}

SCENARIO("Test")
{
    REQUIRE( func(4) == 8 );
}
