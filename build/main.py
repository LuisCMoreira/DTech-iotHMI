import jsonRead as jRead
import csvLog as Log


print(jRead.get_value_from_nested_key('robotData.robotSpecs.serialN'))

Log.mainLog('stop')