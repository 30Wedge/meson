project('exe wrapper behaviour', 'c')

wrapper = join_paths(meson.current_source_dir(), 'remote_launch.py')
add_test_setup(
  'remote_launch',
  exe_wrapper: [wrapper]
)

exe = executable('prog', 'prog.c')
test('test-prog', exe)
