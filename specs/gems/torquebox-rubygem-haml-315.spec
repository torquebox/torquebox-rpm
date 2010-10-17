%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     haml
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-haml-315
Version: 3.0.15
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: An elegant, structured XHTML/XML templating engine. Comes with Sass, a similar CSS templating engine
URL: http://haml-lang.com/
Source0: http://rubygems.org/gems/haml-3.0.15.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}


%description

      Haml (HTML Abstraction Markup Language) is a layer on top of XHTML or XML
      that's designed to express the structure of XHTML or XML documents
      in a non-repetitive, elegant, easy way,
      using indentation rather than closing tags
      and allowing Ruby to be embedded with ease.
      It was originally envisioned as a plugin for Ruby on Rails,
      but it can function as a stand-alone templating engine.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/haml-3.0.15/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/haml-3.0.15/
%{gem_dir}/cache/haml-3.0.15.gem
%{gem_dir}/specifications/haml-3.0.15.gemspec
%doc %{gem_dir}/doc/haml-3.0.15

%changelog

