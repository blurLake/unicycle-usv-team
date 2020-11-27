from gym.envs.registration import register

register(
    id='unicycle-v0',
    entry_point='unicycle_usv.envs:UnicycleEnv',
)
register(
    id='foo-extrahard-v0',
    entry_point='gym_foo.envs:FooExtraHardEnv',
)