import 'package:flutter/material.dart';
import 'package:frontend/constants.dart';
import 'package:frontend/view/admin/main_dash.dart';
import 'package:frontend/view/home/home_view.dart';

class RouteGenerator {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    final args = settings.arguments;
    switch (settings.name) {
      case Home:
        {
          return MaterialPageRoute(builder: (_) => HomeView());
        }
      case AdminDashb:
        {
          return MaterialPageRoute(builder: (_) => AdminDash());
        }
      default:
        {
          return MaterialPageRoute(builder: (_) => HomeView());
        }
    }
  }
}
