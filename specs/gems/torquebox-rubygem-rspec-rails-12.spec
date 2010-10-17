%global tree_prefix  torquebox-
%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global gem_name     rspec-rails
%global gem_instdir  %{gem_dir}/gems/%{gem_name}-%{version}
%global ruby_abi     1.8-java

Name: torquebox-rubygem-rspec-rails-12
Version: 1.3.2
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
BuildArch: noarch
Summary: rspec-rails 1.3.2
URL: http://rspec.info
Source0: http://rubygems.org/gems/rspec-rails-1.3.2.gem

Provides: %{tree_prefix}rubygem(%{gem_name}) = %{version}

Requires: ruby(abi) = %{ruby_abi}

Requires: %{tree_prefix}rubygem(rspec) >= 1.3.0
Requires: %{tree_prefix}rubygem(rack) >= 1.0.0

%description

Behaviour Driven Development for Ruby on Rails.

%prep

%build

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{gem_dir}
install -m 755 -d %{buildroot}%{gem_dir}/gems/rspec-rails-1.3.2/lib
gem install --local --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies --platform ruby %{SOURCE0}

%clean

rm -rf %{buildroot}

%files

%defattr(-, root, root, -)
%{bin_dir}/
%{gem_dir}/gems/rspec-rails-1.3.2/
%{gem_dir}/cache/rspec-rails-1.3.2.gem
%{gem_dir}/specifications/rspec-rails-1.3.2.gemspec
%doc %{gem_dir}/doc/rspec-rails-1.3.2

%changelog

